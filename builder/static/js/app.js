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


function startHandler(ev) {
    ev.dataTransfer.setData("id", ev.target.id);
    ev.dataTransfer.setData("text", ev.target.innerHTML);
    ev.dataTransfer.effectAllowed = "move";
}

function endHandler(ev) {
    console.log('finished dragging');
}

function dragDrop(ev) {
    ev.preventDefault();
    var id = ev.dataTransfer.getData("id");
    var text = ev.dataTransfer.getData("text");
    var option = document.createElement("option");
    option.value = id;
    option.text = text;
    option.classList.add("module");
    ev.target.appendChild(option);
    ev.target.style.border = "";
}

function dragEnter(ev) {
    ev.target.style.border = "3px dotted red";
}

function dragLeave(ev) {
    ev.target.style.border = "";
}

function allowDrop(event) {
    event.preventDefault();
}