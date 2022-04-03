<template>
  <div class="detail">
    <Navbar />
    <h1 class="text-center mb-10">Detail</h1>
    <main class="mt-3">
    <div class="container">
      <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-3 pt-10 text-center">
              <div class="pt-7 pb-7 my-border" style="background-color: #232320; border-width: 0.1px;">
                <img id="wine-img" src="https://images.vivino.com/thumbs/n5By4_iWSS2Zmf7anQtL_Q_pb_x300.png" alt="...">
              </div>
          </div>
        <div class="col-md-1"></div>
        <div class="col-md-4">
          <div class="shadow-sm" id="info-card">
            <div class="card-body">
              <h5 class="card-title mx-3 pt-1">Dom Pérignon P2 Plénitude Brut Champagne 1995</h5>
              <div class="card-text pt-3 pb-3">
                <h5 class="pt-5 pb-3 border-top"><div class="badge mx-2" id="my-badge">WINERY</div>Dom Pérignon</h5>
                <h5 class="pt-3 pb-3"><div class="badge mx-2" id="my-badge">WINE NAME</div>P2 Plénitude Brut Champagne 1995</h5>
                <h5 class="pt-3 pb-3"><div class="badge mx-2" id="my-badge">WINE TYPE</div>Sparkling</h5>
                <h5 class="pt-3 pb-3"><div class="badge mx-2" id="my-badge">COUNTRY</div>France</h5>
                <h5 class="pt-3 pb-3"><div class="badge mx-2" id="my-badge">GRAPES</div>Chardonnay, Pinot Noir</h5>
                <h5 class="pt-3 pb-3"><div class="badge mx-2" id="my-badge">ALCOHOL</div>12.5</h5>
              <h5 class="card-title pt-5 border-top"> <div class="badge mx-2" id="my-badge">PRICE</div> ￦ 355,917 </h5>
              </div>
            </div>
        
          </div>
        </div>
          <div class="col-md-3" id= "my-detail-card" >
            <div class="fs-4 fw-bold pb-5 pt-3 pl-10" > | 맛 </div>
        <span class="pl-10">당도<badge class="badge" id="taste-badge">1</badge><badge class="badge" id="taste-badge">2</badge>
        <badge class="badge" id="taste-badge">3</badge><badge class="badge bg-warning" id="taste-badge">4</badge>
        <badge class="badge" id="taste-badge">5</badge></span><br />
        <span class="pl-10">산도<badge class="badge" id="taste-badge">1</badge><badge class="badge bg-warning" id="taste-badge">2</badge>
        <badge class="badge" id="taste-badge">3</badge><badge class="badge" id="taste-badge">4</badge>
        <badge class="badge" id="taste-badge">5</badge></span><br />
        <span class="pl-10">바디<badge class="badge" id="taste-badge">1</badge><badge class="badge" id="taste-badge">2</badge>
        <badge class="badge" id="taste-badge">3</badge><badge class="badge bg-warning" id="taste-badge">4</badge>
        <badge class="badge" id="taste-badge">5</badge></span><br />
        <span class="pl-10">타닌<badge class="badge" id="taste-badge">1</badge><badge class="badge" id="taste-badge">2</badge>
        <badge class="badge" id="taste-badge">3</badge><badge class="badge" id="taste-badge">4</badge>
        <badge class="badge" id="taste-badge">5</badge></span>
        <div class="fs-4 fw-bold pb-5 pl-10" > | 향 </div>
        <div style="display:flex;" class="row">
        <span class="col-3 badge ml-11 pt-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white;">brioche</span>
        <span class="col-3 badge ml-3 pt-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white;">honey</span>
        <span class="col-3 badge ml-3 pt-3 mb-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white;">apple</span>
        </div>
        <div class="fs-4 fw-bold pb-5 align-right pt-5 pl-10" > | 어울리는 음식 추천 </div>
        <div class="row" style="display:flex;">
        <span class="col-4 badge ml-11 mb-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white; padding:0px;"><img src="../assets/food/pork.png" style="width:40px; height:40px;" /> Pork </span>
        <span class="col-4 badge ml-11 mb-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white; padding:0px;"><img src="../assets/food/richfish.png" style="width:40px; height:40px;" /> Richfish</span>
        <span class="col-4 badge ml-11 mb-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white; padding:0px;"><img src="../assets/food/shellfish.png" style="width:40px; height:40px;" /> Shellfish</span>
        <span class="col-4 badge ml-11 mb-3 fs-6 text-center" style="border-radius:100px; background-color: rgb(180, 139, 85); color: white; padding:0px;"><img src="../assets/food/soft_cheese.png" style="width:40px; height:40px;" /> Soft Cheese</span>
        </div>
        </div>

          <h1 style="margin-top: 100px; margin-bottom: 50px;"> - 해당 와인과 유사한 와인 추천 - </h1>
           <v-row justify="center" class="mb-5">
      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; color:gainsboro; background-color: #232320; box-shadow: 0 0 10px grey;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: gainsboro">
          <v-img
            :src="require('@/assets/sample/sample1.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

       <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; color:gainsboro; background-color: #232320; box-shadow: 0 0 10px grey;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: gainsboro">
          <v-img
            :src="require('@/assets/sample/sample2.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; color:gainsboro; background-color: #232320; box-shadow: 0 0 10px grey;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: gainsboro">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>

      <v-col cols="3">
          <v-card class="mx-auto" max-width="380"  style="border-radius: 100px; color:gainsboro; background-color: #232320; box-shadow: 0 0 10px grey;" hover outlined>
          <v-btn
        class="mt-10 ml-10"
        text
        icon
        large
        color="red lighten-2"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
      <a href="/detail" style="color: gainsboro">
          <v-img
            :src="require('@/assets/sample/sample3.png')"
            height="300"
            contain
          /><v-img />
          <hr style="border-width: 2px; border-color: pink;"/>
          <v-card-title class="justify-center" style="padding-top: 1px;"><div>Dom Pérignon</div> 
          P2 Plénitude Brut Champagne 1995</v-card-title>
          <v-card-text class="text-center fs-5">#France #Sparkling</v-card-text>
          </a>
        </v-card>
      </v-col>
    </v-row>
      </div>
      </div>
    </main>
  </div>
</template>
<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "Detail",
  components: {
    Navbar,
  },
};
</script>

<style>
#info-card{
  border-style: dashed;
  border-radius: 30px;
  border-width: 5px thick;
  display: flex;
  border-color: burlywood;
}

#wine-img{
  margin-bottom: 10px;
  width: 100px;
  height: 360px;
}


.badge{
  height: 40px;
  text-align: center;
  padding-top: 10px;
  display: block;
  width: 70px;
}

#my-badge{
  height: 40px;
  display: inline;
  padding-bottom: 11px;
  width: 70px;
  text-align: center;
  border-radius: 20px;
  color: whitesmoke;
  background-color: rgb(180, 139, 85);
}

#taste-badge{
  display: inline-flex;
  text-align: center;
  border-radius: 40px;
  width : 30px;
  height: 35px;
  margin-bottom: 2em;
  margin-left: 1em;
  padding-left: 1em;
  background-color: antiquewhite;
  color: maroon;
}

#my-detail-card{
  border-radius: 30px;
  border-style: dashed;
  border-width: 5px thick;
  border-color: burlywood;
  margin-top: 10px;
}

.my-border{
  border: 4px rgba(161, 157, 157, 0.8) ;
  border-style: solid; 
  border-width: 5px;
  border-radius: 100px;
  width: 400px;
}
</style>