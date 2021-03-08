<template>
  <div>
    <el-container>
      <el-header>
        <h1>选择学期</h1>
      </el-header>
      <el-main>
        <!-- 学期选择 -->
        <div>
          <el-radio label="1">上学期</el-radio>
        </div>
        <div>
          <el-radio label="2">下学期</el-radio>
        </div>
        <!-- 下一步 选择单元 -->
        <div style="margin: 100px;"></div>
        <router-link to="/unit">
          <el-button type="primary" round >下一步</el-button>
        </router-link>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "Volume",
};
</script>
