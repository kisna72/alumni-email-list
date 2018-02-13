//Hello


$("#invite_owner").click(function(element){
	url = $(this).attr("data-url")
	email = $("#invite_owner_email").val();
	data = {"email":email}
	$.ajax({
	  type: "POST",
	  url: url,
	  data: data,
	  success: function(msg){
	  	console.log(msg);
	  	$("#invite_owner_message").html(msg);
	  },
	  
	});
	console.log("ajax sent")

})


$("#invite_staff").click(function(element){
	url = $(this).attr("data-url")
	email = $("#invite_staff_email").val();
	data = {"email":email}
	$.ajax({
	  type: "POST",
	  url: url,
	  data: data,
	  success: function(msg){
	  	console.log(msg);
	  	$("#invite_staff_message").html(msg);
	  },
	  
	});
	console.log("ajax sent")

})
