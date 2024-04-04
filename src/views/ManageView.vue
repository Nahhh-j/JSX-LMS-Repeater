<template>
  <div>
 <!-- 이 위는 가장 큰 div (template의 div) -->

    <header class="background">
      <nav class="p-3">
        <div class="d-flex s-between">
         <img src="/src/assets/back_icon.png" class="w-10pc" alt="">
         <img src="/src/assets/calender_icon.png" class="w-10pc" alt="">
        </div>  
      </nav>
      <div>

      </div>

    </header>







 <!-- 이 아래는 가장 큰 div (template의 div) -->
  </div>
</template>

<script setup>

</script>

<style lang="scss" scoped>

.container {
  width: 1194px;
  max-height: 834px;
  margin: 0 auto;
  border: 1px solid black;
  background-color: #F6F8FF;
  overflow: hidden;
}

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