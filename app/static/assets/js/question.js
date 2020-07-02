function stop(){
  let ifr_ids = ['sauce']
    for(let i = 0; i<ifr_ids.length; i++){
      let iframe = document.getElementById(ifr_ids[i]);
      if (iframe != null){
        iframe.src = iframe.src;
      }
    }
}

function prep_yd(hidden_val, submitter){
  $(`#${submitter}`).click(function() {
    alert('clicked');
   $(`#${hidden_val}`).val(3);
});
}

function setQuiz(questions, counter, questionId){
    document.getElementById(questionId[4]).innerHTML = questions.questions[counter];
    document.getElementById(questionId[0]).innerHTML = questions.opt1[counter];
    document.getElementById(questionId[1]).innerHTML = questions.opt2[counter];
    document.getElementById(questionId[2]).innerHTML = questions.opt3[counter];
    document.getElementById(questionId[3]).innerHTML = questions.opt4[counter];
  }
  

  function prep_modal(checker, submitter, hidden_val, questions, questionId, name){
//    $(".modal").each(function() {
      let correct = 0;
      let counter = 0;
      console.log(`The counter is ${counter}`)
      const corrected = document.querySelector(`#${checker}`);
      const submit = document.querySelector(`#${submitter}`);
      

      setQuiz(questions=questions, counter=counter, questionId=questionId);

      $(`#${checker}`).click(function() {
        let rbs = document.querySelectorAll(`input[name=${name}]`); //try string interpolation
        let selectedValue;
        for (const rb of rbs) {
            if (rb.checked) {
                selectedValue = rb.value;
                break;
            }
        }

        if(selectedValue === questions.correct[counter]){
          let cor = document.getElementById(selectedValue);
          cor.classList.add("has-success");
          correct++;
          if(counter == questions.questions.length - 1){
            corrected.disabled = true
            submit.disabled = false

          }
          if (counter < questions.questions.length - 1){
            counter++;
          }
            
          setTimeout(() => { 
            setQuiz(questions=questions, counter=counter, questionId=questionId);
            cor.classList.remove("has-success")
          }, 2000);
          
        } else{
          let inc = document.getElementById(selectedValue);
          let cor = document.getElementById(questions.correct[counter]);
          inc.classList.add("has-danger");
          cor.classList.add("has-success");
          if(counter == questions.questions.length-1){
            corrected.disabled = true
            submit.disabled = false
          }
          if (counter < questions.questions.length-1){
            counter++;
          }  
          setTimeout(() => { setQuiz(questions=questions, counter=counter, questionId=questionId);
            inc.classList.remove("has-danger");
            cor.classList.remove("has-success");
          }, 2000);
          
        }
        // alert("Correct Value is : " +correct) //remove later
        $(`#${hidden_val}`).val(correct);
      });

      
 //   });

  }