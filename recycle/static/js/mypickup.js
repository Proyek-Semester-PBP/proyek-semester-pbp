function posting(e) {
    e.preventDefault()
    
    const name = $("#name_pickup").val()
    const weight = $("#weight_pickup").val()
    const region = $("#reg_pickup").val()
    const city = $("#city_pickup").val()
    const subdistrict = $("#sub_pickup").val()
    const zip_code = $("#zip_pickup").val()
    const detail= $("#addr_pickup").val()
    const description = $("#desc_pickup").val()
    const csrftoken = $("[name=csrfmiddlewaretoken]").val()
    const data_pickup = {
      type: "pickup",
      name: name,
      weight: weight,
      region: region,
      city: city,
      subdistrict: subdistrict,
      zip_code: zip_code,
      detail: detail,
      description: description,
      csrfmiddlewaretoken: csrftoken,
    }
    
    $.ajax({
      type: 'POST',
      url: '/recycle/add_history/',
      data: data_pickup,
      success: function() {
      const point = parseInt($("#weight_pickup").val()) * 5
      Swal.fire(
          'Congratulations, you get ' + point + ' points',
      )
    },
    });

  }

  $(document).ready(() => {
    $("#pickup-btn").click(posting)
  })