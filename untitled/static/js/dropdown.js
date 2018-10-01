var messageTypes = [
    'success',
    'danger'
];

function showNotification(type, message) {
    if (messageTypes.indexOf(type) === -1) {
        type = 'danger';
    }
    $.notify({
        message: message
    }, {
        type: type,
        placement: {
		from: "bottom"
	},
    });
}

$(function () {
    $(".drag-file").draggable({
        helper: "clone",
        cursorAt: {bottom: 5},
        containment: "window",
        zIndex: 100,
        revert: true,
        opacity: 0.7,
    });
    $(".droppable").droppable({
        accept: ".drag-file",
        drop: function (event, ui) {
            $.ajax({
                url: "/category/file/add",
                type: 'POST',
                data: {
                    'categoryId': $(event.target).attr('categoryId'),
                    'categoryName': $(event.target).attr('categoryName'),
                    'filePath': $(ui.draggable[0]).attr('filePath'),
                    'fileName': $(ui.draggable[0]).attr('fileName')
                },
                error: function () {
                    showNotification('danger', 'Something goes wrong. Please try again later.');
                },
                success: function (data) {
                    showNotification(data.success ? 'success' : 'danger', data.message !== undefined ? data.message : '');
                }
            });
        }
    });
});