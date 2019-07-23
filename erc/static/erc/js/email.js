
function postToGoogle() {
                var field1 = $("#nameField").val();

 				
				if(field1 == ""){
					alert('Please Fill Your Name');
					document.getElementById("nameField").focus();
					return false;
				}


				
	
                $.ajax({
                    url: "https://docs.google.com/forms/d/e/1FAIpQLSdhbxjbp1QxaotQYOEbupDbQRvDx8Ku8XHbbh3P4AUJzXgsLA/formResponse?",
					data: {"entry.1636625767": field1},
                    type: "POST",
                    dataType: "xml",
                    success: function(d)
					{
					},
					error: function(x, y, z)
						{

							$('#success-msg').show();
							$('#form').hide();
							
						}
                });
				return false;
            }
        