const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
tableOutput.style.visibility = "hidden";
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");

searchField.addEventListener("keyup", (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length > 0) {
        tbody.innerHTML = "";
        fetch("/car-search", {
                body: JSON.stringify({
                    term: searchValue
                }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                appTable.style.visibility = "hidden";
                tableOutput.style.visibility = "visible";

                console.log("data.length", data.length);

                if (data.length === 0) {
                    noResults.style.visibility = "visible";
                    tableOutput.style.visibility = "hidden";
                } else {
                    noResults.style.visibility = "hidden";
                    data.forEach((item) => {
                        tbody.innerHTML += `
                            <tr>
                            <td>${car.car_id}</td>
                            <td>${car.car_type}</td>
                            <td>${car.num_passengers}</td>
                            <td>${car.Violation.count}</td>
                            <td>${car.car_owner}</td>
                            <td>${car.location}</td>
                            </tr>`;
                    });
                }
            });
    } else {
        tableOutput.style.visibility = "hidden";
        appTable.style.visibility = "visible";
    }
});


(function($) {
    // USE STRICT
    "use strict";
    var navbars = ['header', 'aside'];
    var hrefSelector = 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"])';
    var linkElement = navbars.map(element => element + ' ' + hrefSelector).join(', ');
    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 900,
        outDuration: 900,
        linkElement: linkElement,
        loading: true,
        loadingParentElement: 'html',
        loadingClass: 'page-loader',
        loadingInner: '<div class="page-loader__spin"></div>',
        timeout: false,
        timeoutCountdown: 5000,
        onLoadEvent: true,
        browser: ['animation-duration', '-webkit-animation-duration'],
        overlay: false,
        overlayClass: 'animsition-overlay-slide',
        overlayParentElement: 'html',
        transition: function(url) {
            window.location.href = url;
        }
    });


})(jQuery);

(function($) {
    // Use Strict
    "use strict";
    try {
        var progressbarSimple = $('.js-progressbar-simple');
        progressbarSimple.each(function() {
            var that = $(this);
            var executed = false;
            $(window).on('load', function() {

                that.waypoint(function() {
                    if (!executed) {
                        executed = true;
                        /*progress bar*/
                        that.progressbar({
                            update: function(current_percentage, $this) {
                                $this.find('.js-value').html(current_percentage + '%');
                            }
                        });
                    }
                }, {
                    offset: 'bottom-in-view'
                });

            });
        });
    } catch (err) {
        console.log(err);
    }
})(jQuery);
(function($) {
    // USE STRICT
    "use strict";

    // Scroll Bar
    try {
        var jscr1 = $('.js-scrollbar1');
        if (jscr1[0]) {
            const ps1 = new PerfectScrollbar('.js-scrollbar1');
        }

        var jscr2 = $('.js-scrollbar2');
        if (jscr2[0]) {
            const ps2 = new PerfectScrollbar('.js-scrollbar2');

        }

    } catch (error) {
        console.log(error);
    }

})(jQuery);
(function($) {
    // USE STRICT
    "use strict";

    // Select 2
    try {

        $(".js-select2").each(function() {
            $(this).select2({
                minimumResultsForSearch: 20,
                dropdownParent: $(this).next('.dropDownSelect2')
            });
        });

    } catch (error) {
        console.log(error);
    }


})(jQuery);
(function($) {
    // USE STRICT
    "use strict";

    // Dropdown 
    try {
        var menu = $('.js-item-menu');
        var sub_menu_is_showed = -1;

        for (var i = 0; i < menu.length; i++) {
            $(menu[i]).on('click', function(e) {
                e.preventDefault();
                $('.js-right-sidebar').removeClass("show-sidebar");
                if (jQuery.inArray(this, menu) == sub_menu_is_showed) {
                    $(this).toggleClass('show-dropdown');
                    sub_menu_is_showed = -1;
                } else {
                    for (var i = 0; i < menu.length; i++) {
                        $(menu[i]).removeClass("show-dropdown");
                    }
                    $(this).toggleClass('show-dropdown');
                    sub_menu_is_showed = jQuery.inArray(this, menu);
                }
            });
        }
        $(".js-item-menu, .js-dropdown").click(function(event) {
            event.stopPropagation();
        });

        $("body,html").on("click", function() {
            for (var i = 0; i < menu.length; i++) {
                menu[i].classList.remove("show-dropdown");
            }
            sub_menu_is_showed = -1;
        });

    } catch (error) {
        console.log(error);
    }

    var wW = $(window).width();
    // Right Sidebar
    var right_sidebar = $('.js-right-sidebar');
    var sidebar_btn = $('.js-sidebar-btn');

    sidebar_btn.on('click', function(e) {
        e.preventDefault();
        for (var i = 0; i < menu.length; i++) {
            menu[i].classList.remove("show-dropdown");
        }
        sub_menu_is_showed = -1;
        right_sidebar.toggleClass("show-sidebar");
    });

    $(".js-right-sidebar, .js-sidebar-btn").click(function(event) {
        event.stopPropagation();
    });

    $("body,html").on("click", function() {
        right_sidebar.removeClass("show-sidebar");

    });


    // Sublist Sidebar
    try {
        var arrow = $('.js-arrow');
        arrow.each(function() {
            var that = $(this);
            that.on('click', function(e) {
                e.preventDefault();
                that.find(".arrow").toggleClass("up");
                that.toggleClass("open");
                that.parent().find('.js-sub-list').slideToggle("250");
            });
        });

    } catch (error) {
        console.log(error);
    }


    try {
        // Hamburger Menu
        $('.hamburger').on('click', function() {
            $(this).toggleClass('is-active');
            $('.navbar-mobile').slideToggle('500');
        });
        $('.navbar-mobile__list li.has-dropdown > a').on('click', function() {
            var dropdown = $(this).siblings('ul.navbar-mobile__dropdown');
            $(this).toggleClass('active');
            $(dropdown).slideToggle('500');
            return false;
        });
    } catch (error) {
        console.log(error);
    }
})(jQuery);