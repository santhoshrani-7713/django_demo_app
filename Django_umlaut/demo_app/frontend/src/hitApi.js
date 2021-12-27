

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


const calculateForm = () => {
    let shift_model = parseInt(document.getElementById("shift_model").value, 10) || 0
    let std_shift_time_gross = parseInt(document.getElementById("std_shift_time_gross").value, 10) || 0
    let start_up = parseInt(document.getElementById("start_up").value, 10) || 0
    let break_ = parseInt(document.getElementById("break_").value, 10) || 0
    let lunch = parseInt(document.getElementById("lunch").value, 10)|| 0
    let others = parseInt(document.getElementById("others").value, 10) || 0
    let days_weeks = parseInt(document.getElementById("days_weeks").value, 10) || 0
    let weeks = parseInt(document.getElementById("weeks").value, 10) || 0

    let break_time = start_up + break_ + lunch + others
    let shift_net = std_shift_time_gross - break_time
    console.log(break_time, shift_net)
    console.log(start_up, break_, lunch, others, std_shift_time_gross, break_time)

    document.getElementById("total_break_time").value = `${break_time}`
    document.getElementById("std_shift_time").value = `${shift_net}`
}