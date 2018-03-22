class CreateYourplans < ActiveRecord::Migration[5.1]
  def change
    create_table :yourplans do |t|
      t.belongs_to :student, foreign_key: true
      t.integer :courses
      t.integer :schedule_id

      t.timestamps
    end
  end
end
