$(document).ready(function() {
    if ($('div').is("#topmenu_enter_text")) {
        $('#topmenu_enter').hover(
        function() {
            $('#topmenu_enterbox').css('display', 'inline-block');
            $('#topmenu_enter').css('color', '#89a6aa');
        },
        function() {
            $('#topmenu_enterbox').css('display', 'none');
            $('#topmenu_enter').css('color', '#f8f8f8');
            $('#topmenu_enterbox').hover(
            function() {
                $('#topmenu_enterbox').css('display', 'inline-block');
                $('#topmenu_enter').css('color', '#89a6aa');
            },
            function() {
                $('#topmenu_enterbox').css('display', 'none');
                $('#topmenu_enter').css('color', '#f8f8f8');
            });
        });
    } else {
        $('#profile').hover(
        function() {
            $('#profile_logo').attr('src', '/static/pictures/person_blue.png');
        },
        function() {
            $('#profile_logo').attr('src', '/static/pictures/person.png');
        });
        $('#logout').hover(
        function() {
            $('#logout_logo').attr('src', '/static/pictures/exit_blue.png');
        },
        function() {
            $('#logout_logo').attr('src', '/static/pictures/exit.png');
        });
    }

    $('#topmenu_enterwith_vk').hover(
    function() {
        $(this).attr('src', '/static/pictures/vk_blue.png');
    },
    function() {
        $(this).attr('src', '/static/pictures/vk.png');
    });
});
