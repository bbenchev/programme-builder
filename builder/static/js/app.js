$("input[type='checkbox']").change(function() {
    if (this.checked) {
        $.ajax({
        type: "GET",
        url: "/get_criteria",
        data: $(this).val(),
        success : function(response) {
            $.each(response.criteria, function(index,value) {
                var li = $("<li class=criterion></li>").text(value);
                $('.criteria-list').append(li);
            })
        }
        });
    }
    else {
        $('.criteria-list').empty();
    }
});
