$('#searchform').submit( function(e) {
    e.preventDefault();

    document.location = $("#searchinput").val();

    });