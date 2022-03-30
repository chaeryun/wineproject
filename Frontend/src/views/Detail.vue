<template>
  <div class="home">
    <Navbar />
    <h1 class="text-center">Detail</h1>
    <main class="mt-3">
    <div class="container">
      <div class="row">
        <div class="col-md-5">
            <div class="carousel-inner">
              <div class="">
                <img src="https://images.vivino.com/thumbs/n5By4_iWSS2Zmf7anQtL_Q_pb_x300.png" class="d-block mt-4" alt="...">
              </div>
          </div>
        </div>
        <div class="col-md-7">
          <div class="card shadow-sm">
            <div class="card-body">
              <h5 class="card-title">Dom Pérignon P2 Plénitude Brut Champagne 1995</h5>
              <h5 class="card-title pt-3 pb-3 border-top">355,917원</h5>
              <p class="card-text border-top pt-3">
                <span class="badge bg-primary">Sparkling</span>
                <span class="badge bg-dark">France</span>
                <span class="badge bg-dark">Chardonnay, Pinot Noir</span>
                <span class="badge bg-dark">12.5</span>
              </p>
              <p class="card-text pb-3">
                
              </p>
            </div>
          </div>
        </div>
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
