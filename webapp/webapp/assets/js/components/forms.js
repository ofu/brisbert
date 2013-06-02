$(function() {

  var textBoxWidth = $(".form--story__text").val().length;
  $(".form--story__text").width(textBoxWidth * 18 + "px");

  $(".form--story__text").autoGrowInput({
      comfortZone: 40,
      minWidth: 40,
      maxWidth: 320
  });

  $(".form--story__text").focus(function() {
    this.select();
  });

  $(".form--story__text").mouseup(function(e){
    e.preventDefault();
  });
});
