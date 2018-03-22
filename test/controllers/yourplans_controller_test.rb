require 'test_helper'

class YourplansControllerTest < ActionDispatch::IntegrationTest
  setup do
    @yourplan = yourplans(:one)
  end

  test "should get index" do
    get yourplans_url
    assert_response :success
  end

  test "should get new" do
    get new_yourplan_url
    assert_response :success
  end

  test "should create yourplan" do
    assert_difference('Yourplan.count') do
      post yourplans_url, params: { yourplan: { courses: @yourplan.courses, schedule_id: @yourplan.schedule_id, student_id: @yourplan.student_id } }
    end

    assert_redirected_to yourplan_url(Yourplan.last)
  end

  test "should show yourplan" do
    get yourplan_url(@yourplan)
    assert_response :success
  end

  test "should get edit" do
    get edit_yourplan_url(@yourplan)
    assert_response :success
  end

  test "should update yourplan" do
    patch yourplan_url(@yourplan), params: { yourplan: { courses: @yourplan.courses, schedule_id: @yourplan.schedule_id, student_id: @yourplan.student_id } }
    assert_redirected_to yourplan_url(@yourplan)
  end

  test "should destroy yourplan" do
    assert_difference('Yourplan.count', -1) do
      delete yourplan_url(@yourplan)
    end

    assert_redirected_to yourplans_url
  end
end
