class AddCourseIdToSchedules < ActiveRecord::Migration[5.1]
  def change
    add_reference :schedules, :course, index: true
  end
end
