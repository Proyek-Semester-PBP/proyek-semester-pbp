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
        fetchData()
        const point = parseInt($("#weight_drop").val()) * 5
        Swal.fire(
            'Congratulations, you get ' + point + ' points',
        )
      },
    });
    }

    function update(result) {
      const myElement = $("#history-table");
      myElement.html('');
      for (let i = 0; i < result.length; i++) {
          var myData = result[i].fields;
          myElement.append(
              `<tr>`+
                  `<td>`+myData.name+`</td>`+
                  `<td>`+myData.date+`</td>`+
                  `<td>`+myData.location+`</td>`+
                  `<td>`+myData.weight+` grams</td>`+
                  `<td>`+myData.description+`</td>`+
              `</tr>`
          );
      }
  }

    function fetchData() {
      $.get("/recycle/json/", update)
    }

    $(document).ready(() => {
        $("#dropoff-btn").click(posting)
    })