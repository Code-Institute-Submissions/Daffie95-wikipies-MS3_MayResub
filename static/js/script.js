$(document).ready(function () {
    // function to activate mobile sidenav
    $(".sidenav").sidenav({ edge: "right" });
    // function to active collapsible to be clickable
    $('.collapsible').collapsible();
    // function to activate tooltip on hover
    $('.tooltipped').tooltip('outDuration', 150);
});