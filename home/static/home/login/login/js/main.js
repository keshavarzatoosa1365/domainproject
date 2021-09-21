$(document).ready(function () {
    updateContainer();
    $(window).resize(function() {
        updateContainer();
    });
});
function updateContainer() {
	if ($(window).width() < 600) {
		$("#call").attr('href',"tel:096790");
		$("#tel").hover(function()
			{
				$(this).css({"background":"url(/img/telgold2.png)"});
				$("#login").css({"width":"440px"});
				$("#arrow").css({"margin-right":"20px"});
				$("#txt").css({"color":"#665600"});
			},function()
			{
				$(this).css({"background":"url(/img/tel2.png)"});
				$("#login").css({"width":"420px"});
				$("#arrow").css({"margin-right":"10px"});
				$("#txt").css({"color":"#4c6805"});
			});
    }
    else{
    	$("#call").attr('href',"tel:096790");
    	$("#tel").hover(function()
			{
				$(this).css({"background":"url(/img/telgold.png)"});
				$("#login").css({"width":"440px"});
				$("#arrow").css({"margin-right":"20px"});
				$("#txt").css({"color":"#665600"});
			},function()
			{
				$(this).css({"background":"url(/img/tel.png)"});
				$("#login").css({"width":"420px"});
				$("#arrow").css({"margin-right":"10px"});
				$("#txt").css({"color":"#4c6805"});
			});
	} 

}
