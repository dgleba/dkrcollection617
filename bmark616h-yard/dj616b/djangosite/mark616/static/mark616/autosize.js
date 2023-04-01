
// version 01

// I didn't get this to work. 2023-02-27.
// https://stackoverflow.com/questions/50143415/add-a-javascript-file-to-django-admin
// https://stackoverflow.com/questions/34662266/is-there-a-method-to-autofit-each-textarea-to-the-size-of-its-data-returned-fro



$(window).on('resize', function(e) {
  $('textarea[data-autoresize]').each(function() {
    var $textarea = $(this);
    $textarea.css('height', 'auto');
    $textarea.css('height', $textarea.prop('scrollHeight') + 'px');
  });
})

$('textarea[data-autoresize]').each(function() {
  $(this).on('keyup input change paste propertychange', function(e) {
    var $textarea = $(this);
    $textarea.css('height', 'auto');
    $textarea.css('height', $textarea.prop('scrollHeight') + 'px');
  });
});
