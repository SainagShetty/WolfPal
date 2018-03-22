class AddCToAverageGrades < ActiveRecord::Migration[5.1]
  def change
    add_column :average_grades, :syllabus_id, :integer
  end
end
