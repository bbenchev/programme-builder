$("input[type='checkbox']").change(function() {
    var id = $(this).val();
    if (this.checked) {
        $("#" + id).show();
    }
    else {
        $("#" + id).hide();
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

    criteria = document.getElementsByClassName("criterion")
    $.ajax({
        type: "GET",
        url:  "/ajax/check_fulfilled/" + id,
        success: function(response) {
            var items = response.criteria;
            for (item in items) {
                for (criterion in criteria) {
                    if (items[item] == criteria[criterion].innerHTML) {
                        criteria[criterion].style.color = "green";
                    }
                }
            }
        }
    })
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