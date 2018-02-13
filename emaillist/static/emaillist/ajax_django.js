// Author : Krishna Regmi
// How to Use it ?  See the example below. 
        //Start the loader
//        $(this).prepend('<p class="saving_message">saving</p>');
//
//       ajax_upload({
//            url:"/livingcity/new/",
//            data:data,
//            on_success:success,
//            on_fail:fail,
//            current_dom: current_dom_element,
//            });
//    
//        //alert(new_tour_title);
//        console.log(new_tour_title);
//    });
//    function success(data, current_dom){
//        $(current_dom).children(".saving_message").remove();
//        //alert("success" + data + ";" + current_dom);
//    }
//    function fail(current_dom){
//        $(current_dom).children(".saving_message").remove();
//        $(current_dom).prepend('<p class="saving_message error_message" style="font:1em;">saving failed </p>' );
//    }
//
//
//
//
//
//

function ajax_upload(arguments){
    var a = arguments;
    $.ajax({
            url: arguments.url || '',
            type: arguments.type || 'POST',
            data: arguments.data || 'NO DATA',
            cache: false,
            //dataType: 'json',
            processData: false, //Don't process the files. prevents converion to string
            contentType: false, //
            success: function(data, textStatus, jqXHR)
            {
                var server_sends = data
                if(typeof data.error === 'undefined')
                {
                    a.on_success(server_sends, a.current_dom);
                }
                else
                {
                    alert("Operation Failed.")
                    //alert('Error' + data.error);
                }
            },
            error: function(jqXHR, textStatus, errorThrown)
            {
                a.on_fail(a.current_dom);
                //alert('Error : ' + textStatus + ' errorThrown:   ' + errorThrown)
                //Stop Loading Spinner
            },
        });

}

//This function gets cookie with a given name
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//The functions below will create a header with csrftoken

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});