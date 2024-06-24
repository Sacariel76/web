$(function () {
    $('#btnAgregar').click(function () {
        $.ajax({
            url: '/exec_agregar',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
