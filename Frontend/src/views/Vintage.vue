<template>
  <div class="vintage pt-5">
    <Navbar />
    <h1 class="fw-bold mb-5">Vintage</h1>
    <h6 class="text-center"> 원하는 지역 / 연도 / 포도품종을 골라 날씨 빅데이터를 기반으로 VINTAGE한 와인을 추천 받아주세요!</h6>
  <div class="form-group justify-center border-top border-bottom mt-3 mb-3">
    <select class="form-control secondary" id="productCategory2" ref="productCategory">
      <option value="1">Year</option>
      <option value="2">2021</option>
      <option value="3">2020</option>      
      <option value="4">2019</option>
      <option value="5">2018</option>
      <option value="6">2017</option>
      <option value="7">2016</option>
      <option value="8">2015</option>
      <option value="9">2014</option>
      <option value="10">2013</option>
      <option value="11">2012</option>
      <option value="12">2011</option>
      <option value="13">2010</option>
      <option value="14">2009</option>
      <option value="15">2008</option>
      <option value="16">2007</option>
      <option value="17">2006</option>
      <option value="18">2005</option>
      <option value="19">2004</option>
      <option value="20">2003</option>
    </select>
    <select class="form-control secondary" id="productCategory2" ref="productCategory">
      <option value="1">Country</option>
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
    <select class="form-control secondary" id="productCategory2" ref="productCategory">
      <option value="1">Grapes</option>
      <option value="2">Chardonnay</option>      
      <option value="3">Touriga Nacional</option>
      <option value="4">Pinot Noir</option>
      <option value="5">Touriga Franca</option>
      <option value="6">Tinta Roriz</option>
      <option value="7">Cabernet Sauvignon</option>
      <option value="8">mTinta Barroca</option>
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

  <div class="select-wine">
    <button type="submit" id="searchWine" class="btn btn-warning">
    <img src="../assets/find.png" id="find-icon" class="pb-2" alt="" /></button>
  </div>
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
                <h1 class="text-center">👑 인기 1위 </h1>
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
						<div class="col-lg-6 col-md-5">
							<div class="hero-area-content">
								<img src="@/assets/sample/sample2.png" alt="poster" />
							</div>
						</div>
						<div class="col-lg-6 col-md-7">
							<div class="hero-area-content pr-50">
								<h1 class="text-center">👑 인기 2위 </h1>
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
						<div class="col-lg-6 col-md-5">
							<div class="hero-area-content">
								<img src="@/assets/sample/sample3.png" alt="_poster" />
							</div>
						</div>
						<div class="col-lg-6 col-md-7">
							<div class="hero-area-content pr-50">
								<h1 class="text-center">👑 인기 3위 </h1>
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
.hero-area-slide {
    background: #1b1d29a6;
    margin: 70px 15px 50px !important; 
    padding-top: 52px;
    box-shadow: 0 0 20px #000000;
    max-width: 650px;
}

.hero-area-content > img {
    position: relative;
    margin-top: -120px;
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