<template>
  <div>
    <p class="title">Yu Hsuan's resume</p><br>
    <p class="intros1">Major in Infromation and Computer Engineering</p><br><br>
    <p class="intros2">Programming Languages :</p><br><br>
    <p class="intros3">C, C++, C#, Java, Python, HTML, CSS, JavaScript</p><br><br>
    <p class="intros2">Tools and Others:</p><br><br>
    <p class="intros3">Git, Heroku, Vue.js (Basic), Linux, MySQL</p><br><br>
    <p class="intros2">Communities:</p><br><br>
    <p class="intros3">SITCON, Chatbot Taiwan</p><br><br>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.title{
    font-size: 54px;
    color: #c39ea0;
    margin: 5px 0;
    position: center;
    bottom:30px;
    right: 50px;
}
.intros1{
    margin: 5px 0;
    position: absolute;
    left: 10px;
    color: #c39ea0;
    font-size: 30px;
}
.intros2{
    margin: 5px 0;
    position: absolute;
    left: 10px;
    color: #f0d632;
    font-size: 30px;
}
.intros3{
    margin: 5px 0;
    position: absolute;
    left: 10px;
    color: #939597;
    font-size: 30px;
}
</style>
