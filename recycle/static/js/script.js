$(document).ready(() => {
    $.ajax({
        url : "/recycle/json/",
        success : function(result) {
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
    });
});