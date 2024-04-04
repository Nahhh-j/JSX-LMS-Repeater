<template>
  <div>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-header display">
            <img class="profile" img src="/src/assets/profile_content.jpg"></img>
            <!-- <div class="modal-margin"> -->
              <div style="margin-right: 10px;">
              <div style="font-size:40px; color: white;" class="font-bold"><b>권인구</b></div>
              <div style="font-size:20px; color: white;" class="font-middle">출석기록 : 9/365일</div>
              </div>
              <section class="univ-logos">
                <img src="/src/assets/snu_logo.png" class="univ-img">
                <img src="/src/assets/ysu_logo.png" class="univ-img">
                <img src="/src/assets/kaist_logo.png" class="univ-img">
              </section>
            <!-- </div> -->


            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <img src="/src/assets/study_check.png" width="700px" class="shadow" style="margin: 10px 0 20px 30px"></img>
          </div>
        </div>
      </div>
    </div>



    <div class="community-container">
    <div class="display">
<!-- 작성자 프로필 -->
      <div>
        <img class="profile" img src="/src/assets/profile_content.jpg" data-bs-toggle="modal" data-bs-target="#exampleModal">
      </div>
<!-- 작성자명, 작성 날짜 -->
      <div class="margin">
        <div style="font-size:40px;" class="font-bold"><b>권인구</b></div>
        <div style="font-size:20px;" class="font-middle">2024년 4월 3일 13:00</div>
      </div>
    </div>

<!-- 게시글 본문 -->
      <div style="margin: 8px 0 8px 30px; font-size: 18px;" class="font-middle">
          질문이 있습니다. 답변 가능하신 분 설명해주시면 감사하겠습니다!
          <br>
          정비례는 x의 값이 2배가 될 때 y의 값이 2배가 된다는데 이 관계식이 어째서 y=ax인 건지 이해가 안 돼요. 
          <br>
          x가 11, a가 2고 y를 10으로 본다면 x값이 2배가 될 때 y값은 20이 되잖아요. y=ax는 x가 a배일 때 값과 
          <br>
          y값은 같다로 밖에 해석이 안되네요.. 이해가 쉽도록 상세하게 답변해주시면 감사하겠습니다.
      </div>

<!-- 이미지, 과목명 태그 -->
    <div>
      <div style="margin: 20px 0 8px 30px;" class="display justify-content-between">
        <div style="position: relative;">
          <img src="/src/assets/test2.jpg" width="70px" class="shadow"></img>

          <div style="position: absolute; top: 0px; left: 50px;">
            <img src="/src/assets/test1.jpg" width="70px" class="shadow"></img>
          </div>
        </div>
        <div class="tag font-middle" style="color: coral;"> 수학 </div>
      </div>
    </div>

<!-- 댓글/공유 아이콘, 답글 개수 -->
      <div style="margin: 30px 0 0 30px; font-size: 25px; color: grey;">
        <div class="display">
          <i class="fa-regular fa-message"></i>
          <div style="margin-right: 20px;"></div>
          <i class="fa-solid fa-share-from-square"></i>
          <div class="comment font-middle">답글 3개</div>
        </div>
      </div>

      <hr>

<!-- 댓글 입력창 -->
    <div style="width: 775px; margin-left: 25px; font-size: 18px; position: relative;" class="font-middle">
    <form action="" class="display">
        <button class="send-button" style="position: absolute; top: 8px; right: 0;z-index: 100;">
            <img src="/src/assets/send.png">
        </button>
        <input type="text" placeholder="내용을 입력해주세요" class="comment-input" style="position: relative;">
    </form>
</div>

<!-- 댓글창 -->
    <div>
      <div class="comment-container" style="margin-left: 25px;">
        <div class="display">
          <img class="comment-profile" src="/src/assets/profile_comment.jpg" style="border: 1px solid lightgrey;">
        <div style="font-size:20px; margin-top: 17px;" class="font-middle"><b>박은지</b></div>
        <div class="comment-comment font-middle" style="font-size: 15px;">2024년 4월 3일 14:00</div>
        </div>

          <div style="margin: 0 18px 3px 18px; font-size: 18px;" class="font-middle">안녕하세요, 인구님! overflow 속성 대신에 overflow-x 속성이나 overflow-y 속성을 사용한다면 가로나  세로만 선택적으로 스크롤바를 보여줄 수 있습니다.</div>
        <div class="display">
          <div style="font-size: 20px; margin: 0 0 0 18px; color: grey;"><i class="fa-regular fa-message"></i></div>
          <div style="margin: 0 0 0 660px; color: grey;" class="font-middle">답글 1개</div>
        </div>
        </div>
    </div>

<!-- 대댓글창 -->
    <div>
      <div class="comment-comment-container">
        <div class="display">
          <img class="comment-profile" src="/src/assets/profile_content.jpg" style="border: 1px solid lightgrey;">
        <div style="font-size:20px; margin-top: 17px;" class="font-middle"><b>권인구</b></div>
        <div class="comment-comment-comment font-middle" style="font-size: 15px;">2024년 4월 3일 14:20</div>
        </div>

          <div style="margin: 0 18px -6px 18px; font-size: 18px;" class="font-middle">안녕하세요, 은지님! 친절한 설명 감사합니다. 그런데 요소의 콘텐츠가 너무 길어서 개발자가 원하는 블록 크기를 넘어갈 때,
사용하는 속성은 무엇일까요?</div>
        <div class="display">
          <div style="font-size: 20px; margin: 10px 0 0 18px; color: grey;"><i class="fa-regular fa-message"></i></div>
          <div style="margin: 10px 0 0 580px; color: grey;" class="font-middle">답글 0개</div>
        </div>  
      </div>
    </div>

    <br>

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

// modal style
.modal-header{
  width: 100%;
  height: 160px;
  background-color: #00068E;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
  border-bottom-left-radius: 20px;
  border-bottom-right-radius: 20px;
}

.univ-logos{
  background-color: rgb(204, 204, 204);
  width: 350px;
  // box-shadow: 2px 4px 4px rgb(212, 203, 203);
  border-radius: 15px;
  padding: 2%;
  margin: 20px 0 20px 20px;
  justify-content: space-evenly;
}

.univ-img{
  background-color: white;
  border-radius: 50%;

  width: 80px;
  height: 80px;
  margin-left: 20px;

  position: relative;
}

// content style
.font-bold{
  font-family: "Pretendard Variable";
  font-weight: bold;
}

.font-middle{
  font-family: "Pretendard Variable";
  font-weight: middle;
}

.font-light{
  font-family: "Pretendard Variable";
  font-weight: light;
}

.profile{
  border-radius: 100px;
  width: 150px;
  padding: 20px;
}

.comment-profile{
  border-radius: 100px;
  width: 50px;
  padding: 3px;
  margin: 10px;
}

.tag{
  margin: 68px 30px 0 0;
  border-radius: 15px;
  height: 35px;
  width: 70px;
  background-color: rgb(255, 239, 241);
  text-align: center;
  font-size: 20px;
  border: 10px;
}

.shadow{
  box-shadow: 5px 5px 5px 5px black;
  border-radius: 10px;
}

.margin{
  margin-top: 23px;
}

.modal-margin{
  margin-top: 10px;
}

.community-container{
  background-color: rgba(255, 255, 255, 0.5);
  // opacity: 60%;
  // border: 1px solid ;
  box-shadow: 4px 4px 4px 4px lightgrey;
  border-radius : 10px;
  width: 850px;
  height: 665px;
  margin-top: -2%;
  margin-right: 5%;
  float: right;
  overflow-y: auto;
}

.comment-container{
  background-color: white;
  box-shadow: 1px 1px 1px 1px lightgrey;
  border-radius : 10px;
  width: 775px;
  height: 175px;
  margin-top: 13px;
}

.comment-comment-container{
  background-color: white;
  box-shadow: 1px 1px 1px 1px lightgrey;
  border-radius : 10px;
  width: 700px;
  height: 175px;
  margin: 13px 0 0 96px;
}

.comment{
  margin-left: 620px;
  font-size: 20px;
}

.comment-comment{
  margin-left: 485px;
  margin-top: 22px;
  font-size: 20px;
}

.comment-comment-comment{
  margin-left: 409px;
  margin-top: 22px;
  font-size: 20px;
}

.display{
  display: flex;
}

.comment-input{
  width:800px;
  height:50px;
  font-size:15px;
  border-radius: 15px;
}

.send-button{
  border: none;
  outline: none;
  background-color: inherit ;
  cursor: pointer;
}
</style>