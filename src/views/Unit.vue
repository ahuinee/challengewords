<template>
  <div>
    <el-container>
      <el-header>
        <h1>选择单元</h1>
      </el-header>
      <el-main>
        <!-- 单元选择 -->
        <div v-for="(item, index) in units" :key="index">
          <el-radio
            style="margin-top: 10px"
            v-model="selectedUnitIndex"
            :label="index"
            >{{ item.unitName }}</el-radio
          >
        </div>
        <!-- 单词挑战 -->
        <el-button style="margin: 100px" type="primary" round @click="pushWord"
          >下一步</el-button
        >
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Unit",
  data() {
    return {
      units: [],
      selectedUnitIndex: 0,
    };
  },
  created() {
    this.units = this.$route.params.units;
  },
  methods: {
    // 进入单元选择
    pushWord() {
      const words = this.units[this.selectedUnitIndex].words;
      console.log(words);
      this.$router.push({ name: "Word", params: { words: words } });
    },
  },
};
</script>
