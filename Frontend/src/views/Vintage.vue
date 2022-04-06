<template>
  <div class="vintage">
    <!-- <Navbar /> -->
    <!-- <h1 class="fw-bold mb-5">Vintage</h1> -->
    <h1 class="text-center pt-13">날씨 기반 빅데이터로 추천하는<br /> 2019 / 2020 / 2021해의 Good Vintage Wine Top3</h1>
  <div class="form-group justify-center mt-3 mb-3">
    <button class="food-button" style="height: 50px;">2019</button>
    <button class="food-button" style="height: 50px;">2020</button>
    <button class="food-button" style="height: 50px;">2021</button>
    </div>

  	<!-- hero area start -->
			<!-- 인기1위 -->
		<section class="hero-area" id="home">
			<div class="container">
				<div class="hero-area-slider">
					<div class="row hero-area-slide">
						<div class="col-lg-6 col-md-5">
							<div class="hero-area-content">
								<img src="@/assets/sample/sample1.png" />
							</div>
						</div>
						<div class="col-lg-6 col-md-7">
							<div class="hero-area-content pr-50">
                <h1 class="text-center">👑 Top 1 </h1>
                <hr />
								<h3 class="text-center">P2 Plénitude Brut Champagne 1995</h3>
                <hr>
									<p class="fs-5 fw-bold text-center">Wine Type / <span class="fs-6 fw-normal">Sparkling</span></p> 
									<p class="fs-5 fw-bold text-center">Winery / <span class="fs-6 fw-normal">Dom Pérignon</span></p> 
									<p class="fs-5 fw-bold text-center">Grapes / <span class="fs-6 fw-normal">Chardonnay, Pinot Noir</span></p>
									<p class="fs-5 fw-bold text-center">Country / <span class="fs-6 fw-normal">France</span></p>  
									<p class="fs-5 fw-bold text-center">Price / <span class="fs-6 fw-normal">￦ 355,917</span></p>  
                <button class="btn btn-warning" id="go-to-detail"> Details.. </button>     
								<br> 
							</div>
						</div>
					</div>
          </div>
					<!-- 인기 2위 -->
          <div class="hero-area-slider2">
					<div class="row hero-area-slide" id="second-vintage">
						<div class="col-lg-5 col-md-4">
							<div class="hero-area-content">
								<img src="@/assets/sample/sample2.png" alt="poster" />
							</div>
						</div>
						<div class="col-lg-6 col-md-7">
							<div class="hero-area-content pr-50">
								<h1 class="text-center">👑 Top 2 </h1>
                <hr />
								<h3 class="text-center">P2 Plénitude Brut Champagne 1995</h3>
                <hr>
									<p class="fs-5 fw-bold text-center">Wine Type / <span class="fs-6 fw-normal">Sparkling</span></p> 
									<p class="fs-5 fw-bold text-center">Winery / <span class="fs-6 fw-normal">Dom Pérignon</span></p> 
									<p class="fs-5 fw-bold text-center">Grapes / <span class="fs-6 fw-normal">Chardonnay, Pinot Noir</span></p>
									<p class="fs-5 fw-bold text-center">Country / <span class="fs-6 fw-normal">France</span></p>  
									<p class="fs-5 fw-bold text-center">Price / <span class="fs-6 fw-normal">￦ 355,917</span></p>
                  <button class="btn btn-warning justify-center" id="go-to-detail"> Details.. </button>        
									<br>
							</div>
						</div>
					</div>
					<!-- 인기3위 -->
					<div class="row hero-area-slide" id="third-vintage">
						<div class="col-lg-5 col-md-4">
							<div class="hero-area-content">
								<img src="@/assets/sample/sample3.png" alt="_poster" />
							</div>
						</div>
						<div class="col-lg-6 col-md-7">
							<div class="hero-area-content pr-50">
								<h1 class="text-center">👑 Top 3 </h1>
                <hr />
								<h3 class="text-center">P2 Plénitude Brut Champagne 1995</h3>
                <hr>
									<p class="fs-5 fw-bold text-center">Wine Type / <span class="fs-6 fw-normal">Sparkling</span></p> 
									<p class="fs-5 fw-bold text-center">Winery / <span class="fs-6 fw-normal">Dom Pérignon</span></p> 
									<p class="fs-5 fw-bold text-center">Grapes / <span class="fs-6 fw-normal">Chardonnay, Pinot Noir</span></p>
									<p class="fs-5 fw-bold text-center">Country / <span class="fs-6 fw-normal">France</span></p>  
									<p class="fs-5 fw-bold text-center">Price / <span class="fs-6 fw-normal">￦ 355,917</span></p>
                  <button class="btn btn-warning" id="go-to-detail"> Details.. </button>  
									<br>
							</div>
						</div>
					</div>
				</div>	
      </div>
		</section><!-- hero area end -->

  </div>
</template>
<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "Vintage",
  components: {
    Navbar,
  },
}
</script>

<style>
#productCategory2{
  align-content: center;
  color : white;
  border-radius: 2em;
  text-align: center;
  height: 50px;
  width: 300px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px, rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}

#go-to-detail{
  height: 40px;
  margin:auto;
  display:block;
  width: 100px;
}
.select-wine{
  margin-top: 14px;
}

#find-icon{
  width: 45px;
  height: 45px;
}

#second-vintage{
  float: left;
  max-width: 550px;
}

#third-vintage{
  float: right;
  max-width: 550px;
}

/* hero-area */

.hero-area {
    position: relative;
    color: white;
    background-image: url('../assets/hero-area.png');
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
    overflow: hidden;
}

.vintage{
  color: white;
  background-image: url('../assets/hero-area.png');
}

.hero-area-slide {
    background: #1b1d29a6;
    margin: 70px 15px 50px !important; 
    padding-top: 52px;
    box-shadow: 0 0 20px #000000;
    max-width: 650px;
}

.hero-area-content > img {
    position: relative;
    margin-top: -90px;
}
.hero-area-slider {
	margin: auto;
  text-align: center;
  display: flex;
  justify-content: center;
}
.hero-area-slider2 {
  text-align: center;
}

.hero-area-content h3 {
    margin-top: 35px;
}

</style>