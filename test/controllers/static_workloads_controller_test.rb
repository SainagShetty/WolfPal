require 'test_helper'

class StaticWorkloadsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @static_workload = static_workloads(:one)
  end

  test "should get index" do
    get static_workloads_url
    assert_response :success
  end

  test "should get new" do
    get new_static_workload_url
    assert_response :success
  end

  test "should create static_workload" do
    assert_difference('StaticWorkload.count') do
      post static_workloads_url, params: { static_workload: { assignments: @static_workload.assignments, core: @static_workload.core, exams: @static_workload.exams, project: @static_workload.project, syllabus_id: @static_workload.syllabus_id } }
    end

    assert_redirected_to static_workload_url(StaticWorkload.last)
  end

  test "should show static_workload" do
    get static_workload_url(@static_workload)
    assert_response :success
  end

  test "should get edit" do
    get edit_static_workload_url(@static_workload)
    assert_response :success
  end

  test "should update static_workload" do
    patch static_workload_url(@static_workload), params: { static_workload: { assignments: @static_workload.assignments, core: @static_workload.core, exams: @static_workload.exams, project: @static_workload.project, syllabus_id: @static_workload.syllabus_id } }
    assert_redirected_to static_workload_url(@static_workload)
  end

  test "should destroy static_workload" do
    assert_difference('StaticWorkload.count', -1) do
      delete static_workload_url(@static_workload)
    end

    assert_redirected_to static_workloads_url
  end
end
