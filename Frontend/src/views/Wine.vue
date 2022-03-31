<template>
  <div class="wine">
    <h1>Wine</h1>
    <hr />
    <form v-on:submit.prevent="registerProduct()" enctype="multipart/form-data">
      <label for="productCategory"> | Wine Search </label>
      <div class="form-group">
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">와인 타입</option>
          <option value="2">1. Red</option>
          <option value="3">2. White</option>
          <option value="4">3. Sparkling</option>
          <option value="5">4. Rose</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">국가</option>
          <option value="2">1. 프랑스 / France</option>
          <option value="3">2. 미국 / United States</option>
          <option value="4">3. 이탈리아 / Italy</option>
          <option value="5">4. 스페인 / Spain</option>
          <option value="6">5. 호주 / Australia</option>
          <option value="7">6. 남아프리카공화국 / South Africa</option>
          <option value="8">7. 오스트리아 / Austria</option>
          <option value="9">8. 독일 / Germany</option>
          <option value="10">9. 아르헨티나 / Argentina</option>
          <option value="11">10. 그리스 / Greece</option>
          <option value="12">11. 칠레 / Chile</option>
          <option value="13">12. 뉴질랜드 / New Zealand</option>
          <option value="14">13. 브라질 / Brazil</option>
          <option value="15">14. 조지아 / Georgia</option>
          <option value="16">15. 루마니아 / Romania</option>
          <option value="17">16. 스위스 / Switzerland</option>
          <option value="18">17. 캐나다 / Canada</option>
          <option value="19">18. 슬로베니아 / Slovenia</option>
          <option value="20">19. 이스라엘 / Israel</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">포도품종</option>
          <option value="2">1. Chardonnay</option>
          <option value="3">2. Touriga Nacional</option>
          <option value="4">3. Pinot Noir</option>
          <option value="5">4. Touriga Franca</option>
          <option value="6">5. Tinta Roriz</option>
          <option value="7">6. Cabernet Sauvignon</option>
          <option value="8">7. mTinta Barroca</option>
          <option value="9">8. Grenache</option>
          <option value="10">9. Tinto Cao</option>
          <option value="11">10. Shiraz/Syrah</option>
          <option value="12">11. Merlot</option>
          <option value="13">12. Cinsault</option>
          <option value="14">13. Mourvedre</option>
          <option value="15">14. Cabernet Franc</option>
          <option value="16">15. Pinot Meunier</option>
          <option value="17">16. Souzao</option>
          <option value="18">17. Tinta Amarela</option>
          <option value="19">18. Malbec</option>
          <option value="20">19. Touriga Francesa</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">가격대</option>
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
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">향</option>
          <option value="2">1. Citrus</option>
          <option value="3">2. Oak</option>
          <option value="4">3. Strawberry</option>
          <option value="5">4. Leather</option>
          <option value="6">5. Brioche</option>
          <option value="7">6. Blackberry</option>
          <option value="8">7. Apple</option>
          <option value="9">8. Honey</option>
          <option value="10">9. Minerals</option>
          <option value="11">10. Chocolate</option>
          <option value="12">11. Peach</option>
          <option value="13">12. Raisin</option>
          <option value="14">13. Plum</option>
          <option value="15">14. Caramel</option>
          <option value="16">15. Vanilla</option>
          <option value="17">16. Butter</option>
          <option value="18">17. Tobacco</option>
          <option value="19">18. Cherry</option>
          <option value="19">19. Earthy</option>
        </select>
      </div>
      <label for="productCategory"> | Wine Style </label>
      <div class="form-group">
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">당도</option>
          <option value="2">1</option>
          <option value="3">2</option>
          <option value="4">3</option>
          <option value="5">4</option>
          <option value="6">5</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">산도</option>
          <option value="2">1</option>
          <option value="3">2</option>
          <option value="4">3</option>
          <option value="5">4</option>
          <option value="6">5</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">바디</option>
          <option value="2">1</option>
          <option value="3">2</option>
          <option value="4">3</option>
          <option value="5">4</option>
          <option value="6">5</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">타닌</option>
          <option value="2">1</option>
          <option value="3">2</option>
          <option value="4">3</option>
          <option value="5">4</option>
          <option value="6">5</option>
        </select>
        <select
          class="form-control success"
          id="productCategory"
          ref="productCategory"
        >
          <option value="1">음식궁합</option>
          <option value="2">1. Shellfish / 조개류, 갑각류</option>
          <option value="3">2. Pork / 돼지고기</option>
          <option value="4">3. Beef / 소고기</option>
          <option value="5">4. Mild and Soft Cheese / 부드러운 치즈</option>
          <option value="6">5. Poultry / 닭, 오리, 거위</option>
          <option value="7">6. Richfish / 부자건어물</option>
          <option value="8">7. Lamb / 양고기</option>
          <option value="9">8. Pasta / 파스타</option>
          <option value="10">9. Mature and Hard Cheese / 딱딱한 치즈</option>
          <option value="11">10. Salmon / 연어</option>
          <option value="12">11. Cured Meat / 절인 고기</option>
          <option value="13">12. Tuna / 참치</option>
          <option value="14">13. Vegetarian / 채식</option>
          <option value="15">14. Aperitif / 식전주, 반주</option>
          <option value="16">15. Veal / 송아지 고기</option>
          <option value="17">
            16. Appetizers and Snacks / 애피타이저 및 과자
          </option>
          <option value="18">17. Blue Cheese / 블루 치즈</option>
          <option value="19">18. Spicy Food / 매운 음식</option>
          <option value="20">19. Sweet Dessert / 달콤한 디저트</option>
        </select>
      </div>
      <div class="select-input">
        <input
          type="text"
          class="form-control"
          id="wineName"
          placeholder="와인 이름을 검색해주세요."
          ref="wineName"
        />
        <button type="submit" id="searchWine" class="btn btn-success">
          찾기
        </button>
      </div>
    </form>
    <hr />

    <v-container id="wine-card">
      <v-row justify="space-around">
        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>

        <v-card width="400">
          <v-img
            height="200px"
            src="https://www.keumyang.com/mall/shop_image_new/202102/1613698451_FreixenetCordonNegro.png"
            contain
          >
          </v-img>

          <v-card-text>
            <v-timeline align-top dense>
              <v-timeline-item
                v-for="info in infos"
                :key="info.name"
                :color="info.color"
                small
              >
                <div>
                  <div>{{ info.winery }}</div>
                </div>
                <div class="font-weight-normal">
                  <strong>{{ info.name }}</strong>
                </div>
                <div>
                  <div>{{ info.hashtag }}</div>
                </div>
              </v-timeline-item>
            </v-timeline>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn icon>
              <v-icon>mdi-heart</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-row>
    </v-container>
  </div>
</template>
<script>
export default {
  name: "Wine",

  data: () => ({
    infos: [
      {
        winery: `Dom Pérignon`,
        name: " P2 Plénitude Brut Champagne 1995",
        hashtag: "#France #Sparkling",
        color: "deep-purple lighten-1",
      },
    ],
  }),
};
</script>

<style>
.form-group {
  display: flex;
}

label {
  margin-left: 1em;
  font-weight: bold;
}

select {
  margin: 1em;
}

h1 {
  text-align: center;
}

#productCategory {
  color: white;
  border-radius: 2em;
  text-align: center;
  height: 50px;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 50px 100px -20px,
    rgba(0, 0, 0, 0.3) 0px 30px 60px -30px;
}

option {
  border-radius: 2em;
}

.select-input {
  display: flex;
  margin: 1em;
}

button {
  color: white;
  width: 90px;
  height: 50px;
}

#wineName {
  width: 900px;
  border-radius: 2em;
  height: 50px;
  margin-right: 1em;
}

#searchWine {
  border-radius: 2em;
  color: white;
}

hr {
  border-style: dashed;
  border-color: green;
  margin: 30px;
}

#wine-card {
  display: flex;
}

v-card {
  padding: 2em;
}
</style>
