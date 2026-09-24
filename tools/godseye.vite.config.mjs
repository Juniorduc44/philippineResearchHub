import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { createBrowserViteConfig } from './gods-eye-view/build/vite.js';
import { localProviderPlugins } from './gods-eye-view/server/providers/local.js';
import { apiNotFoundPlugin } from './gods-eye-view/server/standalone/api-not-found.js';

const appRoot = fileURLToPath(new URL('./gods-eye-view/', import.meta.url));

function applyDotEnv(dir) {
  let text = '';
  try {
    text = readFileSync(`${dir}/.env`, 'utf8');
  } catch {
    return;
  }
  for (const raw of text.split('\n')) {
    const line = raw.trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq < 1) continue;
    const key = line.slice(0, eq).trim();
    let value = line.slice(eq + 1).trim();
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1);
    }
    if (process.env[key] === undefined) process.env[key] = value;
  }
}

function publicBase() {
  const raw = (process.env.GEV_PUBLIC_BASE || '/proxy/4173/').trim() || '/';
  if (raw === './' || raw === '.') return './';
  return raw.endsWith('/') ? raw : `${raw}/`;
}

/**
 * Hub overlay so the globe works in code-server Simple Browser.
 * Interface: http://localhost:8080/proxy/4173/
 */
export default function godseyeViteConfig() {
  applyDotEnv(appRoot);

  const cfg = createBrowserViteConfig({
    plugins: [...localProviderPlugins(), apiNotFoundPlugin()],
    googleApiKey: process.env.GOOGLE_MAPS_API_KEY,
    cesiumToken: process.env.CESIUM_ION_TOKEN,
    host: process.env.HOST || '127.0.0.1',
    port: process.env.PORT || 4173,
  });

  const base = publicBase();
  cfg.root = appRoot;
  cfg.base = base;
  cfg.server = cfg.server || {};
  cfg.server.allowedHosts = true;

  if (process.env.GEV_ALLOW_FRAME === '1') {
    cfg.server.headers = {
      'Content-Security-Policy':
        "frame-ancestors 'self' http://localhost:* http://127.0.0.1:*",
    };
  }

  const hmrPort = process.env.GEV_HMR_CLIENT_PORT;
  if (hmrPort) {
    cfg.server.hmr = {
      protocol: process.env.GEV_HMR_PROTOCOL || 'ws',
      host: process.env.GEV_HMR_HOST || 'localhost',
      clientPort: Number.parseInt(hmrPort, 10),
      path: process.env.GEV_HMR_PATH || base.replace(/\/$/, ''),
    };
  }

  const prefix = base === './' ? '' : base.replace(/\/$/, '');

  cfg.plugins = [
    {
      name: 'hub-code-server-proxy',
      configureServer(server) {
        server.middlewares.use((req, res, next) => {
          if (!req.url || !prefix) return next();
          const url = req.url;
          // Direct :4173/ → the prefixed app (what Simple Browser uses).
          if (url === '/' || url === '') {
            res.statusCode = 302;
            res.setHeader('Location', `${prefix}/`);
            res.end();
            return;
          }
          // code-server /proxy/4173/ strips the prefix. Put it back so Vite
          // `base` matches what the browser requested.
          if (!url.startsWith(prefix) && !url.startsWith('/@id')) {
            req.url = prefix + (url.startsWith('/') ? url : `/${url}`);
          }
          next();
        });
      },
    },
    ...(cfg.plugins || []),
  ];

  return cfg;
}
