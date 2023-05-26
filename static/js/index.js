function aboutUs() {


    // productdef = productdefdt.rows().data().toArray()
    
    
    
    $.ajax({
      headers: {'X-CSRFToken': '{{ csrf_token }}'},
      type: "POST",
      url: "/aboutUs/",
      data: {
          
          'userid':'aboutusviewpost',
          
    
      },
      success: function (response, textStatus, xhr) {
       
    
        console.log(response.data);
        Userinterest = response.data
        
        userinterestdt.ajax.reload();
       
      },
      error: function (xhr, ajaxOptions, thrownError) {
       console.log("aboutUserror");
        
        // SlideNotification('Error!',xhr.responseJSON.message,'error')
      },
      });
    }

//     function getCol()
// {
//     // var table = document.getElementById('tbl');
//     var column = ["ok"];
//     // for(var i = 0; i<table.rows.length; i++){
//     //     column.push(table.rows[i].cells[1].childNodes[0].value);
//     // }
//     alert(column)
//     $.ajax({
//         headers: {'X-CSRFToken': '{{ csrf_token }}'},
//         url: '/get_custom_bingo',
//         type: 'POST',
//         data: {'arr':column}
//       });
// }

// let loginForm = document.getElementById("loginForm");

// loginForm.addEventListener("submit", (e) => {
//   e.preventDefault();

//   let username = document.getElementById("username");
//   let password = document.getElementById("password");

//   if (username.value == "" || password.value == "") {
//     alert("Ensure you input a value in both fields!");
//   } else {
//     // perform operation with form input
//     alert("This form has been successfully submitted!");
//     console.log(
//       `This form has a username of ${username.value} and password of ${password.value}`
//     );

//     username.value = "";
//     password.value = "";
//   }
// });

// $('#UploadConversionFile').submit(function (e) { // catch the form's submit event
//   e.preventDefault();

//   if (document.getElementById("myfileToConversion").value == "") {
//     SlideNotification('Error!', 'Please Select The File!', 'error')
//   } else {

//     Swal.fire({
//       title: 'Are you sure?',
//       text: "You Want To Upload!",
//       icon: 'warning',
//       showCancelButton: true,
//       confirmButtonColor: '#3085d6',
//       cancelButtonColor: '#d33',
//       confirmButtonText: 'Yes, Upload it!'
//     }).then((result) => {
//       if (result.isConfirmed) {

//         loading("Uploading File..")
//         let formData = new FormData(this);
//         formData.append('Conversion_Exchange', $('#SelectConversionExchage').val());

//         $.ajax({ // create an AJAX call...
//           data: formData,
//           type: $(this).attr('method'), // GET or POST
//           url: $(this).attr('action'), // the file to call

//           success: function (response, textStatus, xhr) {
//             Swal.close()
//             Swal.fire('Success!', xhr.responseJSON.message, 'success')

//           },

//           error: function (xhr, ajaxOptions, thrownError) {
//             console.log(xhr.responseJSON);
//             Swal.close()

//           },
//           cache: false,
//           contentType: false,
//           processData: false
//         });


//       }
//     })

//   }

// });