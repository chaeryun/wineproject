<template>
  <div class="wine">
    <Navbar />
    <h1>Wine</h1>
    <hr />
    <form v-on:submit.prevent="registerProduct()" enctype="multipart/form-data">
    <label for="productCategory"> | Wine Search </label>
  <div class="form-group">
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">와인 타입</option>
      <option value="2">Red</option>
      <option value="3">White</option>      
      <option value="4">Sparkling</option>
      <option value="5">Rose</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">국가</option>
      <option value="2">France </option>
      <option value="3">United States</option>      
      <option value="4">Italy</option>
      <option value="5">Spain</option>
      <option value="6">Australia</option>
      <option value="7">South Africa</option>
      <option value="8">Austria</option>
      <option value="9">Germany</option>
      <option value="10">Argentina</option>
      <option value="11">Greece</option>
      <option value="12">Chile</option>
      <option value="13">New Zealand</option>
      <option value="14">Brazil</option>
      <option value="15">Georgia</option>
      <option value="16">Romania</option>
      <option value="17">Switzerland</option>
      <option value="18">Canada</option>
      <option value="19">Slovenia</option>
      <option value="20">Israel</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">포도품종</option>
      <option value="2">Chardonnay</option>      
      <option value="3">Touriga Nacional</option>
      <option value="4">Pinot Noir</option>
      <option value="5">Touriga Franca</option>
      <option value="6">Tinta Roriz</option>
      <option value="7">Cabernet Sauvignon</option>
      <option value="8">Tinta Barroca</option>
      <option value="9">Grenache</option>
      <option value="10">Tinto Cao</option>
      <option value="11">Shiraz/Syrah</option>
      <option value="12">Merlot</option>
      <option value="13">Cinsault</option>
      <option value="14">Mourvedre</option>
      <option value="15">Cabernet Franc</option>
      <option value="16">Pinot Meunier</option>
      <option value="17">Souzao</option>
      <option value="18">Tinta Amarela</option>
      <option value="19">Malbec</option>
      <option value="20">Touriga Francesa</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">가격</option>
      <option value="2">1만원 이하</option>      
      <option value="3">1만원 ~ 3만원</option>
      <option value="4">3만원 ~ 5만원</option>
      <option value="5">5만원 ~ 7만원</option>
      <option value="6">7만원 ~ 10만원</option>
      <option value="7">10만원 ~ 20만원</option>
      <option value="8">20만원 ~ 50만원</option>
      <option value="9">50만원 ~ 100만원</option>
      <option value="10">100만원 이상</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">향</option>
      <option value="2">Citrus</option>      
      <option value="3">Oak</option>
      <option value="4">Strawberry</option>
      <option value="5">Leather</option>
      <option value="6">Brioche</option>
      <option value="7">Blackberry</option>
      <option value="8">Apple</option>
      <option value="9">Honey</option>
      <option value="10">Minerals</option>
      <option value="11">Chocolate</option>
      <option value="12">Peach</option>
      <option value="13">Raisin</option>
      <option value="14">Plum</option>
      <option value="15">Caramel</option>
      <option value="16">Vanilla</option>
      <option value="17">Butter</option>
      <option value="18">Tobacco</option>
      <option value="19">Cherry</option>
      <option value="19">Earthy</option>
    </select>
  </div>
  <label for="productCategory"> | Wine Style </label>
  <div class="form-group">
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">당도</option>
      <option value="2">1</option>
      <option value="3">2</option>      
      <option value="4">3</option>
      <option value="5">4</option>
      <option value="6">5</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">산도</option>
      <option value="2">1</option>
      <option value="3">2</option>      
      <option value="4">3</option>
      <option value="5">4</option>
      <option value="6">5</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">바디</option>
      <option value="2">1</option>      
      <option value="3">2</option>
      <option value="4">3</option>
      <option value="5">4</option>
      <option value="6">5</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">타닌</option>
      <option value="2">1</option>      
      <option value="3">2</option>
      <option value="4">3</option>
      <option value="5">4</option>
      <option value="6">5</option>
    </select>
    <select class="form-control secondary" id="productCategory" ref="productCategory">
      <option value="1">음식궁합</option>
      <option value="2">Shellfish</option>      
      <option value="3">Pork</option>
      <option value="4">Beef</option>
      <option value="5">Mild and Soft Cheese</option>
      <option value="6">Poultry</option>
      <option value="7">Richfish</option>
      <option value="8">Lamb</option>
      <option value="9">Pasta</option>
      <option value="10">Mature and Hard Cheese</option>
      <option value="11">Salmon</option>
      <option value="12">Cured Meat</option>
      <option value="13">Tuna</option>
      <option value="14">Vegetarian</option>
      <option value="15">Aperitif</option>
      <option value="16">Veal</option>
      <option value="17">Appetizers and Snacks</option>
      <option value="18">Blue Cheese</option>
      <option value="19">Spicy Food</option>
      <option value="20">Sweet Dessert</option>
    </select>
  </div>
  <div class="select-input">
    <input type="text" class="form-control" id="wineName" placeholder="와인 이름을 검색해주세요." ref="wineName">
    <button type="submit" id="searchWine" class="btn btn-warning">
    <img src="../assets/find.png" id="find-icon" class="pb-2" alt="" /></button>
  </div>
</form>
<hr />

<v-container>
    <v-row class="pa-5-mt-1 text-h7 pt-10 pb-5" justify="center" height="200">
    </v-row>
    <v-row justify="center" >
      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined rounded
        
            @click="goDetail"
        >
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    
    <v-row class="pa-5-mt-1 text-h7 pt-10 pb-5" justify="center" height="200">
    </v-row>
    <v-row justify="center">
      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="3">
        <v-card class="mx-auto" max-width="350" hover outlined>
          <v-btn
        class="ma-2"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="400"
            contain
          /><v-img />
          <v-card-title class="justify-center">wine name</v-card-title>
          <v-card-text class="text-center">wine text</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

  </v-container>

</div>
</template>
<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "Wine",
  components: {
    Navbar,
  },
  methods: {
    goDetail() {
      this.$router.push("/detail");
    },
  },
    };
</script>

<style>
.form-group{
  display: flex;
}

label{
  margin-left:1em;
  font-weight: bold;
}

select{
  margin: 1em;
}

#productCategory{
  color : white;
  border-radius: 2em;
  text-align: center;
  height: 50px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}

option{
  border-radius: 2em;
}

.select-input{
  display: flex;
  margin: 1em;
}

button{
  color:white;
  width: 90px;
  height: 50px;
}

#wineName{
  width: 900px;
  border-radius: 2em;
  height: 50px;
  margin-right: 1em;
}

#searchWine{
  border-radius: 2em;
  color: white;
}

hr{
  border-style: dashed;
  border-color: green;
  margin : 30px;
}

v-card{
  padding: 2em;
}

</style>