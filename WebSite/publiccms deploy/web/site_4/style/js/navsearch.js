$(function () {
    $('body, #nav-search button[type="reset"]').on('click keyup', function (event) {
        if (event.which == 27 && $('#nav-search.active').hasClass('active') ||
            $(event.currentTarget).attr('type') == 'reset') {
            closeNavSearch();
        }
    });

    function closeNavSearch() {
        var $form = $('#nav-search.active')
        $form.find('input').val('');
        $form.removeClass('active');
    }

    $(document).on('click', '#nav-search:not(.active) button[type="submit"]', function (event) {
        event.preventDefault();
        if ($(".navbar-toggler").css("display") == "none") {
            var $input = $("#nav-search").find('input');
            $("#nav-search").addClass('active');
            $input.focus();
        }
        else {
            var $input = $("#nav-search").find('input');
            window.location.href = "/dynobjs/search.htm?q=" + $input.val();
        }

    });

    $(document).on('click', '#nav-search.active button[type="submit"]', function (event) {
        event.preventDefault();
        var $input = $("#nav-search").find('input');
        window.open("/dynobjs/search.htm?q=" + $input.val());
    });

    $(document).on('keypress', '#nav-search input', function (event) {
        if (event.keyCode == 13) {
            event.preventDefault();
            var $input = $("#nav-search").find('input');
            window.location.href = "/dynobjs/search.htm?q=" + $input.val();
        }
    });
});