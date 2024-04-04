<template>
  <div>
    <div class="container">
    <div class="display">
      <div>
        <img class="profile" img src="/src/assets/profile_content.jpg">
      </div>
      <div class="margin">
        <div style="font-size:40px;"><b>권인구</b></div>
        <div style="font-size:20px;">2024년 4월 3일 13:00</div>
      </div>
    </div>
      <div style="margin: 18px;">
          질문이 있습니다. 답변 가능하신 분 설명해주시면 감사하겠습니다!
          <br>
          정비례는 x의 값이 2배가 될 때 y의 값이 2배가 된다는데 이 관계식이 어째서 y=ax인 건지 이해가 안 돼요.
          <br>
          x가 1이고 a가 2고 y를 10으로 본다면 x값이 2배가 될 때 y값은 20이 되잖아요. y=ax는 x가 a배일 때 값과 
          <br>
          y값은 같다로밖에 해석이 안되네요.. 이해가 쉽도록 상세하게 답변해주시면 감사하겠습니다.
      </div>

      <div style="margin: 18px;">
        <div style="position: relative;">
          <img src="/src/assets/test2.jpg" width="70px" class="shadow"></img>

          <div style="position: absolute; top: 0px; left: 50px;">
              <img src="/src/assets/test1.jpg" width="70px" class="shadow"></img> 
          </div>
          <div> [수학] </div>

        </div>
      </div>

      <div style="margin: 20px; font-size: 25px; color: grey;">
        <div class="display">
          <i class="fa-regular fa-message"></i>
          <div style="margin-right: 20px;"></div>
          <i class="fa-solid fa-share-from-square"></i>
          <div class="comment">답글 3개</div>
        </div>
      </div>

      <hr>

<!-- 댓글 입력창 -->
    <div style="width: 775px;">
        <form action="">
        <div class="display"><input type="text" placeholder="내용을 입력해주세요" style="width:800px;height:50px;font-size:15px;">
        <input type="submit" style="width: 50px;height: 50px; float: right;"></div>
        </form>
    </div>

<!-- 댓글창 -->
    <div>
      <div class="comment-container">
        <div class="display">
          <img class="comment-profile" src="/src/assets/profile_comment.jpg" style="border: 1px solid black;">
        <div style="font-size:20px; margin-top: 20px;"><b>박은지</b></div>
        <div class="comment-comment" style="font-size: 15px;">2024년 4월 3일 14:00</div>
        </div>

          <div style="margin-left: 18px;">안녕하세요, 인구님! overflow 속성 대신에 overflow-x 속성이나 overflow-y 속성을 사용하면 가로 또는 세로만 선택적으로 스크롤바를 보여줄 수 있습니다.</div>
      
          <div><i class="fa-regular fa-message"></i></div>
      </div>
    </div>




    </div>
  </div>
</template>

<!-- <script>
import data from "@/data"
export default {
  name:"PrCommentCreate",
  props:{
    contentId:Number,
    reload:Function
  },
  data(){
    return{
      context:''
    }
  },
  methods:{
    createComment(){
      data.Comment.push(
          {
            comment_id: data.Comment[data.Comment.length - 1].comment_id + 1,
            user_id: 1,
            content_id: this.contentId,
            context: this.context,
            created_at: '2019-03-29 14:11:11',
            updated_at: null
          }
      )
      this.reload();
      console.log(data.Comment)
    }
  },

}
</script> -->

<style lang="scss" scoped>

.profile{
  border-radius: 100px;
  width: 150px;
  padding: 20px;
}

.comment-profile{
  border-radius: 100px;
  width: 75px;
  padding: 20px;
}

.shadow{
  box-shadow: 5px 5px 5px 5px black;
  border-radius: 10px;
}

.margin{
  margin-top: 23px;
}

.container{
  background-color: lightgrey;
  // border: 1px solid ;
  box-shadow: 3px 3px 3px 3px lightgrey;
  width: 800px;
  height: 680px;
  margin-top: 10%;
  margin-right: 6%;
  float: right;
}

.comment-container{
  background-color: white;
  width: 775px;
  height: 100px;
  margin-top: 13px;
}

.comment{
  margin-left: 580px;
  font-size: 20px;
}

.comment-comment{
  margin-left: 465px;
  margin-top: 20px;
  font-size: 20px;
}

.display{
  display: flex;
}
</style>