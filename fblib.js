function setup(){
	FB.getLoginStatus(function(response){
		if (response.status === 'connected'){
			var uid = response.authResponse.userID;
			var accessToken = response.authResponse.accessToken;
			var a = document.getElementById("uid");
			a.innerHTML=uid;
			var b = document.getElementById("accessToken");
			b.innerHTML=accessToken;
			}
		//else if (response.status === 'not_authorized'){
				//FB.login(function(response){
					//if(response.authResponse){
				//FB.ui();
			}
		else{
		
		}
	}
};

function compare(other){
	var friendsArray;
	$.getJSON("https://graph.facebook.com/me/mutualfriends/" + other, function(data) {
		friendsArray = other;
	});
	return friendsArray;
};


