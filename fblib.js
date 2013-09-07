function setup(){
	FB.getLoginStatus(function(response){
		if (response.status === 'connected'){
			var accessToken = response.authResponse.accessToken;
			$.getJSON($SCRIPT_ROOT + "/POST", accessToken);
		else{	
		}
	})
};

