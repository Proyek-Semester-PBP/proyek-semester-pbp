function posting(e) {
    e.preventDefault()
    const name = $("#name_drop").val()
    const weight = $("#weight_drop").val()
    const location = $("input[type='radio']:checked").val()
    const description = $("#desc_drop").val()
    const csrftoken = $("[name=csrfmiddlewaretoken]").val()

    const data = {
      type: "dropoff",
      name: name,
      weight: weight,
      location: location,
      description: description,
      csrfmiddlewaretoken: csrftoken,
    }
    
    $.ajax({
      type: 'POST',
      url: '/recycle/add_history/',
      data: data,
      success: function() {
        const point = parseInt($("#weight_drop").val()) * 5
        Swal.fire(
            'Congratulations, you get ' + point + ' points',
        )
      },
    });

    }

    $(document).ready(() => {
        $("#dropoff-btn").click(posting)
    })