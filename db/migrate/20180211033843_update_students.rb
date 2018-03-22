class UpdateStudents < ActiveRecord::Migration[5.1]
  def change
    add_column :students, :year, :integer
    add_column :students, :sem, :integer
    remove_column :students, :start_date, :datetime
  end
end
