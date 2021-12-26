

const hit_line_a = () => {

    const URL = "http://127.0.0.1:8000/line_a"

    var formdata = new FormData();
    formdata.append("shift_model", document.getElementById("shift_model").value);
    formdata.append("std_shift_time_gross", document.getElementById("std_shift_time_gross").value);
    formdata.append("start_up", document.getElementById("start_up").value);
    formdata.append("break_time", document.getElementById("break_").value);
    formdata.append("lunch", document.getElementById("lunch").value);
    formdata.append("other", document.getElementById("others").value);
    formdata.append("days_or_week", document.getElementById("days_weeks").value);
    formdata.append("weeks_per_year", document.getElementById("weeks").value);


    var requestOptions = {
    method: 'POST',
    body: formdata,
    redirect: 'follow'
    };
    

    fetch(URL, requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));
    }
