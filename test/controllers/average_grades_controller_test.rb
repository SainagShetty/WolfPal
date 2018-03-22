require 'test_helper'

class AverageGradesControllerTest < ActionDispatch::IntegrationTest
  setup do
    @average_grade = average_grades(:one)
  end

  test "should get index" do
    get average_grades_url
    assert_response :success
  end

  test "should get new" do
    get new_average_grade_url
    assert_response :success
  end

  test "should create average_grade" do
    assert_difference('AverageGrade.count') do
      post average_grades_url, params: { average_grade: { A: @average_grade.A, B: @average_grade.B, C: @average_grade.C, D: @average_grade.D, Other: @average_grade.Other } }
    end

    assert_redirected_to average_grade_url(AverageGrade.last)
  end

  test "should show average_grade" do
    get average_grade_url(@average_grade)
    assert_response :success
  end

  test "should get edit" do
    get edit_average_grade_url(@average_grade)
    assert_response :success
  end

  test "should update average_grade" do
    patch average_grade_url(@average_grade), params: { average_grade: { A: @average_grade.A, B: @average_grade.B, C: @average_grade.C, D: @average_grade.D, Other: @average_grade.Other } }
    assert_redirected_to average_grade_url(@average_grade)
  end

  test "should destroy average_grade" do
    assert_difference('AverageGrade.count', -1) do
      delete average_grade_url(@average_grade)
    end

    assert_redirected_to average_grades_url
  end
end
