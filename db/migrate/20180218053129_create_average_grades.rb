class CreateAverageGrades < ActiveRecord::Migration[5.1]
  def change
    create_table :average_grades do |t|
      t.integer :A
      t.integer :B
      t.integer :C
      t.integer :D
      t.integer :Other

      t.timestamps
    end
  end
end
