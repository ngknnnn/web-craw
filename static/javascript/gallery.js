function  loadImage() {
    const prev = document.querySelector(".prev");
    const next = document.querySelector(".next");
    const page = document.querySelector(".page-num");
    const maxItem =9;
    let index = 1;
    const galleryItems = document.querySelector(".Gallery").children;
    const pagination = Math.ceil(galleryItems.length / maxItem)


    prev.addEventListener("click", function () {
        index--;
        check();
        showItems();
    })
    next.addEventListener("click", function () {
        index++;
        check();
        showItems();
    })

    function check() {
        if (index == pagination) {
            next.classList.add("disabled");
        } else {
            next.classList.remove("disabled");
        }

        if (index == 1) {
            prev.classList.add("disabled");
        } else {
            prev.classList.remove("disabled");
        }
    }

    function showItems() {
        for (let i = 0; i < galleryItems.length; i++) {
            galleryItems[i].classList.remove("show");
            galleryItems[i].classList.add("hide");


            if (i >= (index * maxItem) - maxItem && i < index * maxItem) {
                // if i greater than and equal to (index*maxItem)-maxItem;
                // means  (1*8)-8=0 if index=2 then (2*8)-8=8
                galleryItems[i].classList.remove("hide");
                galleryItems[i].classList.add("show");
            }
            page.innerHTML = index;
        }


    }
}
  window.onload=function(){
    loadImage();
    console.log("asdasd")
  	showItems();
  	check();
  }




//     document.addEventListener("DOMContentLoaded", function() {
//   var lazyloadImages;
//
//   if ("IntersectionObserver" in window) {
//     lazyloadImages = document.querySelectorAll("#img-div");
//     var imageObserver = new IntersectionObserver(function(entries, observer) {
//       entries.forEach(function(entry) {
//         if (entry.isIntersecting) {
//           var image = entry.target;
//           image.src = image.dataset.src;
//           image.classList.remove("img-div");
//           imageObserver.unobserve(image);
//         }
//       });
//     });
//
//     lazyloadImages.forEach(function(image) {
//       imageObserver.observe(image);
//     });
//   } else {
//     var lazyloadThrottleTimeout;
//     lazyloadImages = document.querySelectorAll("#img-div");
//
//     function lazyload () {
//       if(lazyloadThrottleTimeout) {
//         clearTimeout(lazyloadThrottleTimeout);
//       }
//
//       lazyloadThrottleTimeout = setTimeout(function() {
//         var scrollTop = window.pageYOffset;
//         lazyloadImages.forEach(function(img) {
//             if(img.offsetTop < (window.innerHeight + scrollTop)) {
//               img.src = img.dataset.src;
//               img.classList.remove('lazy');
//             }
//         });
//         if(lazyloadImages.length == 0) {
//           document.removeEventListener("scroll", lazyload);
//           window.removeEventListener("resize", lazyload);
//           window.removeEventListener("orientationChange", lazyload);
//         }
//       }, 20);
//     }
//
//     document.addEventListener("scroll", lazyload);
//     window.addEventListener("resize", lazyload);
//     window.addEventListener("orientationChange", lazyload);
//   }
// })
