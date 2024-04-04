<template>
  <div>


<!-- header : jsx 로고 + 알림 벨 -->
    <header>
      <div class="background d-flex s-between p-3 f-50px">
        <img src="/src/assets/로고.png" class="w-10pc" alt="">
        <i class="fa-solid fa-bell p-3 w-10pc white"></i>        
      </div>   
    </header>


<!-- div 안에 좌측/우측으로 나누어 두 개의 div 있음  -->
    <div class="d-flex">

      <!-- 1st div : 좌측 상~하단에 있는 요소  -->
      <div class="w-50pc p-3">
        <section class="d-flex border p-3 m-20px i-center w-80pc">
          <div class="m-20">
            <img src="/src/assets/\profile.jpg" class="w-50px border b-circle">
          </div>
          <div class="p-3">
            '조나희'님<br>반갑습니다! 
            <!-- 이름 있는 부분 함수 처리 -->
          </div>
        </section>
        
        <section class="d-flex border p-3 m-20px s-between">
          <img src="/src/assets/snu_logo.png" class="w-30px b-circle w-10pc" alt="">
          <img src="/src/assets/ysu_logo.png" class="w-30px b-circle w-10pc" alt="">
          <img src="/src/assets/kaist_logo.png" class="w-30px b-circle w-10pc" alt="">
          <div class="w-10pc border b-circle">
            <i class="fa-solid fa-plus i-center h-100pc"></i>
            <!-- + 중앙에 위치시키는 법 모르겠음 ㅠ !!!!!!!!!!!! -->
            <!-- 아 근데 안해도 된다 ㅎㅎ 피그마에 아이콘 있다  -->
          </div>
        </section>
        
        <img src="/src/assets/study_check.png" class="w-100pc p-3" alt="">

      </div>
      
      
      <!-- 2nd div : 우측 상~하단에 있는 요소  -->
      <div class="w-50pc i-center d-column">
        
        <div class="d-flex box b-radius m-20px p-2 background white w-80pc h-30pc">
          <img src="/src/assets/test_icon.png" class="m-20px" alt="">
          <div class="i-center f-30px">모의고사</div>
        </div>
        
        <div class="d-flex box b-radius m-20px p-2 background white w-80pc h-30pc">
          <img src="/src/assets/community_icon.png" class="m-20px" alt="">
          <div class="i-center f-30px">커뮤니티</div>
        </div>
        
        <div class="d-flex box b-radius m-20px p-2 background white w-80pc h-30pc">
          <img src="/src/assets/manage_icon.png" class="m-20px" alt="">
          <div class="i-center f-30px">학습관리</div>
        </div>
        
      </div>
      
    </div>





  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

.background{
  background-color: #00068E
}


.box{
  border: 1px solid black;
}


.b-circle{
  border-radius: 100%;
}

.b-radius{
  border-radius: 10%;
}

.s-between{
    justify-content: space-between;
    }

.i-center{
  display: flex;
  justify-content: center;
  align-items: center;
}

.d-column{
  display: flex;
  flex-direction: column;
}

.white{
  color: white;
}

.m-10px{
  margin: 10px 10px 10px 10px;
}

.m-20px{
  margin: 20px 20px 20px 20px;
}

.w-30px{
  width: 30px;
}

.w-50px{
  width: 50px;
}

.w-10pc{
  width: 10%;
}

.w-15pc{
  width: 15%;
}

.w-20pc{
  width: 20%;
}

.w-30pc{
  width: 30%;
}

.w-40pc{
  width: 40%;
}

.w-50pc{
  width: 50%;
}

.w-80pc{
  width: 80%;
}

.w-100pc{
  width: 100%;
}

.h-30pc{
  height: 30%;
}

.h-100pc{
  height: 100%;
}

.f-30px{
  font-size: 30px;
}

.f-50px{
  font-size: 50px;
}

.f-50pc{
  font-size: 50%;
}


</style>