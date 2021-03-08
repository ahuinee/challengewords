<template>
  <div>
    <el-container>
      <el-header>
        <h1>选择单元</h1>
      </el-header>
      <el-main>
        <!-- 单元选择 -->
        <div>
          <el-radio label="1">第一单元</el-radio>
        </div>
        <div>
          <el-radio label="2">第二单元</el-radio>
        </div>
        <!-- 单词挑战 -->
        <div style="margin: 100px;"></div>
        <router-link to="/word">
          <el-button type="primary" round >开始挑战</el-button>
        </router-link>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Unit",
};
</script>
