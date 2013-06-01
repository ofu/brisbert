$(function() {

  var textBoxWidth = $(".form--story__text").val().length;
  $(".form--story__text").width(textBoxWidth * 24 + "px");

  $(".form--story__text").autoGrowInput({
      comfortZone: 10,
      minWidth: 40,
      maxWidth: 320
  });

  $(".form--story__text").focus(function() {
    this.select();
  });
});
