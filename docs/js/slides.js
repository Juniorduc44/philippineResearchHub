(function () {
  document.querySelectorAll("[data-slides]").forEach(function (root) {
    const imgs = Array.from(root.querySelectorAll(".slides img"));
    if (imgs.length < 2) return;
    const dots = root.querySelector(".slide-dots");
    let i = 0;
    let timer;

    imgs.forEach(function (_, n) {
      const b = document.createElement("button");
      b.type = "button";
      b.setAttribute("aria-label", "Slide " + (n + 1));
      b.addEventListener("click", function (e) {
        e.preventDefault();
        show(n);
        restart();
      });
      dots.appendChild(b);
    });

    function show(n) {
      i = (n + imgs.length) % imgs.length;
      imgs.forEach(function (img, k) {
        img.classList.toggle("is-on", k === i);
      });
      Array.from(dots.children).forEach(function (d, k) {
        d.classList.toggle("is-on", k === i);
      });
    }

    function step(d) {
      show(i + d);
    }

    function restart() {
      clearInterval(timer);
      timer = setInterval(function () {
        step(1);
      }, 4500);
    }

    root.querySelector(".slide-nav.prev").addEventListener("click", function (e) {
      e.preventDefault();
      step(-1);
      restart();
    });
    root.querySelector(".slide-nav.next").addEventListener("click", function (e) {
      e.preventDefault();
      step(1);
      restart();
    });
    root.addEventListener("mouseenter", function () {
      clearInterval(timer);
    });
    root.addEventListener("mouseleave", restart);

    show(0);
    restart();
  });
})();
