<template>
  <div class="detail">
    <Navbar />
    <h1 class="text-center mb-10 fw-bold">Detail</h1>
    <main class="mt-3">
    <div class="container">
      <div class="row">
        <div class="col-md-1"></div>
        <div class="col-md-4 pt-10 text-center">
              <div class="pt-7 pb-7 my-border">
                <img id="wine-img" src="https://images.vivino.com/thumbs/n5By4_iWSS2Zmf7anQtL_Q_pb_x300.png" alt="...">
              </div>
          </div>
        <div class="col-md-7">
          <div class="card shadow-sm" id="info-card">
            <div class="card-body">
              <h5 class="card-title mx-3 pt-1">Dom Pérignon P2 Plénitude Brut Champagne 1995</h5>
              <div class="card-text pt-3 pb-3">
                <h5 class="pt-5 pb-3 border-top"><div class="badge bg-secondary mx-3" id="my-badge">WINERY</div>Dom Pérignon</h5>
                <h5 class="pt-3 pb-3"><div class="badge bg-secondary mx-3" id="my-badge">WINE NAME</div>P2 Plénitude Brut Champagne 1995</h5>
                <h5 class="pt-3 pb-3"><div class="badge bg-secondary mx-3" id="my-badge">WINE TYPE</div>Sparkling</h5>
                <h5 class="pt-3 pb-3"><div class="badge bg-secondary mx-3" id="my-badge">COUNTRY</div>France</h5>
                <h5 class="pt-3 pb-3"><div class="badge bg-secondary mx-3" id="my-badge">GRAPES</div>Chardonnay, Pinot Noir</h5>
                <h5 class="pt-3 pb-3"><div class="badge bg-secondary mx-3" id="my-badge">ALCOHOL</div>12.5</h5>
              <h5 class="card-title pt-5 border-top"> <div class="badge bg-danger mx-3" id="my-badge">PRICE</div> ￦ 355,917 </h5>
              </div>
            </div>
        
          </div>
        </div>
        <div  class="row">
          <div class="col-md-1"></div>
          <div class="col-md-3" id= "my-detail-card" >
            <div class="fs-4 fw-bold pb-10 align-right border-top pt-3 pl-10" > | TASTE </div>
        <span class="pl-10">당도<badge class="badge bg-secondary" id="taste-badge">1</badge><badge class="badge bg-secondary" id="taste-badge">2</badge>
        <badge class="badge bg-secondary" id="taste-badge">3</badge><badge class="badge bg-danger" id="taste-badge">4</badge>
        <badge class="badge bg-secondary" id="taste-badge">5</badge></span><br />
        <span class="pl-10">산도<badge class="badge bg-secondary" id="taste-badge">1</badge><badge class="badge bg-danger" id="taste-badge">2</badge>
        <badge class="badge bg-secondary" id="taste-badge">3</badge><badge class="badge bg-secondary" id="taste-badge">4</badge>
        <badge class="badge bg-secondary" id="taste-badge">5</badge></span><br />
        <span class="pl-10">바디<badge class="badge bg-secondary" id="taste-badge">1</badge><badge class="badge bg-secondary" id="taste-badge">2</badge>
        <badge class="badge bg-secondary" id="taste-badge">3</badge><badge class="badge bg-danger" id="taste-badge">4</badge>
        <badge class="badge bg-secondary" id="taste-badge">5</badge></span><br />
        <span class="pl-10">타닌<badge class="badge bg-secondary" id="taste-badge">1</badge><badge class="badge bg-secondary" id="taste-badge">2</badge>
        <badge class="badge bg-secondary" id="taste-badge">3</badge><badge class="badge bg-secondary" id="taste-badge">4</badge>
        <badge class="badge bg-secondary" id="taste-badge">5</badge></span>
        </div>
          <div class="col-md-4" id= "my-detail-card" > | 음식추천 </div>
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
  border-color: thistle;
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
}

#my-detail-card{
  border-radius: 20px;
  border-style: dashed;
  border-width: 5px ;
  border-color: thistle;
  margin-top: 50px;
}

.my-border{
  border: 4px rgba(161, 157, 157, 0.8) ;
  border-style: solid; 
  border-width: 5px;
  border-radius: 100px;
  width: 400px;
}
</style>