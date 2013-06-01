(function($) {
    $.extend({
        goTo: function(url, params, type) {
                if (typeof options == 'string' && options == 'POST') {
                    var $form = $("<form>")
                        .attr("method", "post")
                        .attr("action", url);
                    $.each(params, function(name, value) {
                        $("<input type='hidden'>")
                            .attr("name", name)
                            .attr("value", value)
                            .appendTo($form);
                    });
                    $form.appendTo("body");
                    $form.submit();
                } else {
                    if (params)
                        document.location = url + '?' + $.param(params);
                    else
                        document.location = url;
                }
            }    
        });
}) (jQuery);